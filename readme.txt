URL

https://app.powerbi.com/links/v58j-CZ187?ctid=33f00146-6fcc-49e9-b568-7896b3069d44&pbi_source=linkShare


Query

select 
    Date
    , count(*) as "User Count"
from 
    data 
group by 
    Date
order by 
    Date
