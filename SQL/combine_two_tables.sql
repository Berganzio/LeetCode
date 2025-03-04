select lastName, firstName, city, state
from Persons p
    left join address a on p.personId = a.personId;