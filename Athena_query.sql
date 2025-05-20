SELECT Country, SUM(Confirmed) as TotalCases
FROM "covid_database"."covid_table"
GROUP BY Country
ORDER BY TotalCases DESC;
