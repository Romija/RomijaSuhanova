--A
SELECT nosaukums FROM gramatas;

--B
SELECT nosaukums, izdosanas_gads FROM gramatas;
--B otrs variants
SELECT nosaukums AS "Grāmatas nosaukums", izdosanas_gads AS "Izdošanas gads"
from gramatas;

--C
SELECT vards FROM autori;

--D
SELECT vards, dzimsanas_gads FROM autori;
--D otrs variants
SELECT vards AS "Autora vārds", dzimsanas_gads AS "Dzimšanas gads"
FROM autori;

--E
SELECT zanrs_nosaukums FROM zanri;
SELECT zanrs_nosaukums FROM zanri ORDER BY zanrs_nosaukums;

--F
SELECT izdevejs_nosaukums FROM izdeveji;
--F otrs variants
SELECT izdevejs_nosaukums AS "Izdevējs" FROM izdeveji;

--G šis uz max skaitu, bet ja * tad nav max punkti pd
SELECT nosaukums,izdosanas_gads FROM gramatas WHERE izdosanas_gads>1950;

--H
SELECT vards, dzimsanas_gads FROM autori WHERE dzimsanas_gads>1950;

--I
SELECT nosaukums, izdosanas_gads FROM gramatas ORDER BY izdosanas_gads;

--J kas parāda tikai tās grāmatas, kuru žanrs ir fantāzija
SELECT gramatas.nosaukums,zanri.zanrs_nosaukums AS zanrs
FROM gramatas
JOIN zanri ON gramatas.zanrs_id=zanri.zanrs_id
WHERE zanri.zanrs_nosaukums='Fantāzija';

--K apvieno tabulas gramatas un autori, lai redzētu, kura grāmata ir kura autora
SELECT gramatas.nosaukums, autori.vards
FROM gramatas
JOIN autori ON gramatas.autors_id = autori.autors_id;

--L apvieno tabulas gramatas, autori un izdeveji, lai redzetu kurš autors un kurš izdevejs ir saistits ar katru gramatu
SELECT gramatas.nosaukums, autori.vards,izdeveji.izdevejs_nosaukums AS izdevejs
FROM gramatas
JOIN autori ON gramatas.autors_id=autori.autors_id
JOIN izdeveji ON gramatas.izdevejs_id=izdeveji.izdevejs_id;

--M kas parāda, cik grāmatu ir katram autoram
SELECT autori.vards, COUNT(gramatas.gramatas_id) AS kopā_grāmatas
FROM autori
JOIN gramatas ON gramatas.autors_id=autori.autors_id
GROUP BY autori.vards;

--N parāda autoru vārdus un to valsti, kuri raksta žanrā "Detektīvi"
SELECT autori.vards, autori.valsts
FROM autori
JOIN gramatas ON gramatas.autors_id=autori.autors_id
JOIN zanri ON gramatas.zanrs_id=zanri.zanrs_id
WHERE zanri.zanrs_nosaukums="Detektīvi";

--O parāda visvecāko un jaunāko izdotās grāmatas nosaukumu un izdošanas gadu
SELECT nosaukums, izdosanas_gads FROM gramatas
WHERE izdosanas_gads=(SELECT MIN(izdosanas_gads)FROM gramatas)
OR izdosanas_gads=(SELECT MAX(izdosanas_gads)FROM gramatas);
