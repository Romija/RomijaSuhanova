--A
SELECT nosaukums FROM gramatas;

--B
SELECT nosaukums, izdosanas_gads FROM gramatas;

--C
SELECT vards FROM autori;

--D
SELECT vards, dzimsanas_gads FROM autori;

--E
SELECT zanrs_nosaukums FROM zanri;

--F
SELECT izdevejs_nosaukums FROM izdeveji;

--G
SELECT nosaukums,izdosanas_gads FROM gramatas WHERE izdosanas_gads>1950;

--H
SELECT vards, dzimsanas_gads FROM autori WHERE dzimsanas_gads>1950;

--I
SELECT nosaukums, izdosanas_gads FROM gramatas ORDER BY izdosanas_gads ASC;

--J


--K
'''SELECT
    autori.vards AS Autors
    gramatas.nosaukums AS Nosaukums,
FROM autori
LEFT JOIN vards ON autori.autors_id = gramatas.autors_id
GROUP BY autori.vards;'''
