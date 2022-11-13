SELECT symbol, SUM(value) AS profit
FROM (
    SELECT symbol, typ, CASE
        WHEN typ='buy' THEN -SUM(value)
        WHEN typ='sell' THEN SUM(value)
    END AS value
    FROM stocks
    GROUP BY symbol, typ
) sub
GROUP BY symbol;
