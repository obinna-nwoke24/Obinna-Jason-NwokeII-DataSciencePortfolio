/*
Author: Obinna Jason Nwoke II
Checking our data
*/
# let's understand our table
select *
from heart_disease.heart;

# Which sex is more likely to get heart disease?
select Sex, avg(HeartDisease) as HeartDisease
from heart_disease.heart
group by Sex
order by avg(HeartDisease) desc;

# Which ChestPainType is more likely to be associated with heart disease?
select ChestPainType, avg(HeartDisease) as HeartDisease
from heart_disease.heart
group by ChestPainType
order by avg(HeartDisease) desc;

# Which RestingECG is more likely to be associated with heart disease?
select RestingECG, avg(HeartDisease) as HeartDisease
from heart_disease.heart
group by RestingECG
order by avg(HeartDisease) desc;

# Which ExerciseAngina is more likely to be associated with heart disease?
select ExerciseAngina, avg(HeartDisease) as HeartDisease
from heart_disease.heart
group by ExerciseAngina
order by avg(HeartDisease) desc;

# Which ST_Slope is more likely to be associated with heart disease?
select ST_Slope, avg(HeartDisease) as HeartDisease
from heart_disease.heart
group by ST_Slope
order by avg(HeartDisease) desc;

# Checking age -> min 28, max 77
# Checking heart disease in different age group
select 
case
when age between 20 and 30 then '20s'
when age between 30 and 40 then '30s'
when age between 40 and 50 then '40s'
when age between 50 and 60 then '50s'
when age between 60 and 70 then '60s'
else '70s' end as AgeGroup, avg(HeartDisease) as HeartDisease
from heart_disease.heart
group by AgeGroup
order by avg(HeartDisease) desc;