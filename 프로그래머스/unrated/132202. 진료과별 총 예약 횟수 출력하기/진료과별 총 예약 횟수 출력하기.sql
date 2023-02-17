-- 코드를 입력하세요
SELECT MCDP_CD '진료과코드', COUNT(MCDP_CD) '5월예약건수
'
FROM APPOINTMENT  
WHERE APNT_YMD IN
    (SELECT APNT_YMD
    FROM APPOINTMENT 
    WHERE APNT_YMD LIKE '%-05-%')
GROUP BY MCDP_CD
ORDER BY COUNT(MCDP_CD), MCDP_CD;    