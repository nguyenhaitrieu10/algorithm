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


select date, price, (
    select avg(t2.price) from stock_tab t2 where t2.date<=t1.date order by t2.date limit 3
    ) as avg_price
from stock_tab t1;
