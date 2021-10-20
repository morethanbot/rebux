-- select *
-- from cat
-- where "recId" = any (select "catalogueRecordID"
--                      from circulation
--                      where "readerID" = 249375);
--
-- select *
-- from cat
-- where "recId" = any (array [31235, 72259, 2389, 971716, 1746903]);
-- --

select *
from cat
where "recId" = any(
    select "catalogueRecordID" from circulation
    where "readerID" = any(
        select "readerID" from circulation where "catalogueRecordID" = any(
            select "catalogueRecordID" from circulation where "readerID" = 231464
            )
        ) order by "finishDate" desc limit 10
    )