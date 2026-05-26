MANUAL_IMAGE_MAP = {
    "PLT-001": "http://localhost:8000/assets/P001_스투키.jpg",
    # PLT-002 고무나무 - 파일 없음
    # PLT-003 금전수 - P025_금전수(자미오쿨카스).jpg 있지만 번호 불일치
    # PLT-004 파키라 - P018_파키라.jpg 있음
    "PLT-004": "http://localhost:8000/assets/P018_파키라.jpg",
    # PLT-005 선인장 - P016_선인장(기둥형).jpg 있음
    "PLT-005": "http://localhost:8000/assets/P016_선인장(기둥형).jpg",
    # PLT-006 스킨답서스 - 파일 없음
    # PLT-007 산세베리아 - 파일 없음
    # PLT-008 아글라오네마 - 파일 없음
    # PLT-009 필로덴드론 - 파일 없음
    "PLT-010": "http://localhost:8000/assets/P006_스파티필름.jpg",
    "PLT-011": "http://localhost:8000/assets/P011_몬스테라.jpg",
    # PLT-012 칼라테아 - 파일 없음
    # PLT-013 보스턴 고사리 - P015_보스턴고사리_컨셉.jpg (컨셉만 있음)
    "PLT-013": "http://localhost:8000/assets/P015_보스턴고사리_컨셉.jpg",
    # PLT-014 아레카야자 - 파일 없음
    "PLT-015": "http://localhost:8000/assets/P019_알로카시아.jpg",
    "PLT-016": "http://localhost:8000/assets/P005_크로톤.jpg",
    "PLT-017": "http://localhost:8000/assets/P020_아이비.jpg",
    "PLT-018": "http://localhost:8000/assets/P021_시클라멘.jpg",
    # PLT-019 동백 - 파일 없음
    "PLT-020": "http://localhost:8000/assets/P024_알로에.jpg",
    # PLT-021 에케베리아 - 파일 없음
    "PLT-022": "http://localhost:8000/assets/P017_유칼립투스.jpg",
    "PLT-023": "http://localhost:8000/assets/P026_틸란드시아.jpg",
    # PLT-024 네프롤레피스 - 파일 없음
    "PLT-025": "http://localhost:8000/assets/P031_싱고니움.jpg",
    # PLT-026 로즈마리 - 파일 없음
    # PLT-027 라벤더 - 파일 없음
    # PLT-028 제라늄 - 파일 없음
    "PLT-029": "http://localhost:8000/assets/P006_스파티필름.jpg",  # 스킨답서스 - 유사 식물로 대체
    # PLT-030 산세베리아 - 파일 없음
    "PLT-031": "http://localhost:8000/assets/P029_행운목(드라세나).jpg",
    "PLT-032": "http://localhost:8000/assets/P022_관음죽.jpg",
}


import asyncio
import os
import re
import uuid
import pandas as pd
from sqlalchemy import delete

from db.session import AsyncSessionLocal
from models.environment_type import EnvironmentType
from models.plant import Plant
from models.recommended_location import RecommendedLocation
from models.mapping import Mapping
from models.categories import Categories
from models.enums import (
    SunlightEnum,
    VentilationEnum,
    TemperatureEnum,
    HumidityEnum,
    ManagementDifficultyEnum,
    SunlightRequirementsEnum,
    SizeEnum,
    AirPurificationEnum,
    PetStabilityEnum,
    LocationEnum,
    CategoryEnum,
    CategoryLevelEnum,
)

excel_path = "사람과초록_식물데이터_v1.xlsx"
ASSETS_DIR = "assets"


def clean_val(val):
    if not isinstance(val, str):
        return val
    return re.sub(r'\(.*?\)', '', val).strip()


def get_enum_member(enum_class, value):
    if pd.isna(value):
        return None
    
    cleaned = clean_val(value)
    
    for member in enum_class:
        if member.value == cleaned:
            return member
            
    for member in enum_class:
        if member.value.replace(" ", "") == cleaned.replace(" ", ""):
            return member

    if '~' in cleaned:
        parts = cleaned.split('~')
        if len(parts) == 2:
            reversed_cleaned = f"{parts[1]}~{parts[0]}"
            for member in enum_class:
                if member.value == reversed_cleaned or member.value.replace(" ", "") == reversed_cleaned.replace(" ", ""):
                    return member
            
    for member in enum_class:
        if member.name.lower() == str(value).strip().lower():
            return member
            
    raise ValueError(f"Value {repr(value)} (cleaned: {repr(cleaned)}) could not be mapped to {enum_class.__name__}")


def get_image_path_map(assets_dir: str, df_plant: pd.DataFrame) -> dict:
    image_map = {}
    if not os.path.exists(assets_dir):
        print(f"Warning: assets 폴더가 없습니다 ({assets_dir})")
        return image_map

    for _, row in df_plant.iterrows():
        plant_id = row['식물 ID']
        name_ko = str(row['식물명 (한글)']).strip()
        if plant_id in MANUAL_IMAGE_MAP:
            image_map[plant_id] = MANUAL_IMAGE_MAP[plant_id]
        else:
            print(f"  Warning: {plant_id} ({name_ko}) 이미지 없음")

    return image_map


async def main():
    print("Reading Excel sheets...")
    
    df_env = pd.read_excel(excel_path, sheet_name='환경유형정의', header=2)
    df_env.columns = df_env.iloc[0]
    df_env = df_env.iloc[1:].reset_index(drop=True)
    df_env = df_env.dropna(subset=['유형 ID'])

    df_kw = pd.read_excel(excel_path, sheet_name='키워드매핑', header=2)
    df_kw.columns = df_kw.iloc[0]
    df_kw = df_kw.iloc[1:].reset_index(drop=True)
    df_kw = df_kw.dropna(subset=['키워드 ID'])

    df_plant = pd.read_excel(excel_path, sheet_name='식물데이터', header=2)
    df_plant.columns = df_plant.iloc[0]
    df_plant = df_plant.iloc[1:].reset_index(drop=True)
    df_plant = df_plant.dropna(subset=['식물 ID'])

    df_matrix = pd.read_excel(excel_path, sheet_name='유형별추천매트릭스', header=2)
    df_matrix.columns = df_matrix.iloc[0]
    df_matrix = df_matrix.iloc[1:].reset_index(drop=True)
    df_matrix = df_matrix.dropna(subset=['식물 ID'])

    # 이미지 맵 로드
    image_path_map = get_image_path_map(ASSETS_DIR, df_plant)
    print(f"이미지 {len(image_path_map)}개 감지됨: {sorted(image_path_map.keys())}")

    async with AsyncSessionLocal() as session:
        async with session.begin():
            print("Deleting existing records...")
            await session.execute(delete(Categories))
            await session.execute(delete(RecommendedLocation))
            await session.execute(delete(Mapping))
            await session.execute(delete(Plant))
            await session.execute(delete(EnvironmentType))
            
            print("Seeding EnvironmentType...")
            env_objects = {}
            for _, row in df_env.iterrows():
                env_id = row['유형 ID']
                env = EnvironmentType(
                    id=env_id,
                    name=row['환경 유형명'],
                    sunlight=get_enum_member(SunlightEnum, row['햇빛']),
                    ventilation=get_enum_member(VentilationEnum, row['통풍']),
                    temperature=get_enum_member(TemperatureEnum, row['온도']),
                    humidity=get_enum_member(HumidityEnum, row['습도']),
                    explanation=row['설명 (사용자에게 표시)'] if pd.notna(row['설명 (사용자에게 표시)']) else None
                )
                session.add(env)
                env_objects[env_id] = env
            
            print("Seeding Mapping...")
            for _, row in df_kw.iterrows():
                env_type_id = row['관련 유형 ID']
                if pd.isna(env_type_id) or str(env_type_id).strip() == '-':
                    env_type_id = None
                
                mapping = Mapping(
                    category=get_enum_member(CategoryEnum, row['카테고리']),
                    keyword_id=row['키워드 ID'],
                    display_keyword=row['키워드 (사용자 표시)'],
                    env_condition=row['관련 환경 조건'] if pd.notna(row['관련 환경 조건']) else None,
                    env_type_id=env_type_id
                )
                session.add(mapping)
                
            print("Seeding Plant...")
            for _, row in df_plant.iterrows():
                plant_id = row['식물 ID']

                image_path = image_path_map.get(plant_id)
                if image_path is None:
                    print(f"  Warning: {plant_id} 이미지 없음")

                plant = Plant(
                    id=plant_id,
                    name_ko=row['식물명 (한글)'],
                    name_en=row['식물명 (영문)'],
                    management_difficulty=get_enum_member(ManagementDifficultyEnum, row['관리 난이도']),
                    watering=row['물주기'],
                    appropriate_temperature=row['적정 온도'],
                    appropriate_humidity=row['적정 습도'],
                    sunlight_requirements=get_enum_member(SunlightRequirementsEnum, row['햇빛 요구량']),
                    size=get_enum_member(SizeEnum, row['크기 분류']),
                    air_purification_effect=get_enum_member(AirPurificationEnum, row['공기정화 효과']),
                    pet_stability=get_enum_member(PetStabilityEnum, row['반려동물 안전']),
                    explanation=row['한줄 설명'] if pd.notna(row['한줄 설명']) else None,
                    image_path=image_path,  # ✅ 추가
                )
                session.add(plant)
                
                locs_str = row['실내 추천 위치']
                if pd.notna(locs_str):
                    locations = [loc.strip() for loc in str(locs_str).split(',') if loc.strip()]
                    for loc in locations:
                        rec_loc = RecommendedLocation(
                            id=str(uuid.uuid4()),
                            plant_id=plant_id,
                            location=get_enum_member(LocationEnum, loc)
                        )
                        session.add(rec_loc)

            print("Seeding Categories Matrix...")
            env_cols = [c for c in df_matrix.columns if c.startswith('ENV-')]
            for _, row in df_matrix.iterrows():
                plant_id = row['식물 ID']
                for col in env_cols:
                    val = row[col]
                    if pd.notna(val) and str(val).strip() in ['O', '△']:
                        env_type_id = col.split('\n')[0].strip()
                        category_level = get_enum_member(CategoryLevelEnum, val)
                        
                        category_entry = Categories(
                            plant_id=plant_id,
                            env_type_id=env_type_id,
                            level=category_level
                        )
                        session.add(category_entry)

        await session.commit()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())