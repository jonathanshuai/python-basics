friend_request
friend_request requester_id, sent_to_id, time

request_accepted
acceptor_id, requestor_id, time


friends
user_id, friend_id

likes
user_id, page_id



friends.user_id  --


SELECT
  friends.user_id,
  friend_likes.page_id
FROM
  likes friend_likes
JOIN
  friends ON (friend_likes.user_id = friends.friend_id)
LEFT JOIN
  likes user_likes (user_likes.user_id = friends.user_id AND user_likes.page_id = friend_likes.page_id)
WHERE
  user_likes.page_id is NULL




Cars
id      int
make    varchar
model   text
n_cyl   int
hp      int


CREATE TABLE Cars(
    id int,
    make varchar(255),
    model varchar(255),
    n_cyl int,
    hp int
)

insert into Cars (id, make, model, n_cyl, hp) values (0, 'Toyota', 'Corolla', 6, 16);
insert into Cars (id, make, model, n_cyl, hp) values (1, 'Honda', 'Odys', 3, 20);
insert into Cars (id, make, model, n_cyl, hp) values (2, 'RAANDO', 'BANDO', 10, 25);
insert into Cars (id, make, model, n_cyl, hp) values (3, 'RAANDO2', 'BANDO2', 12, 25);
insert into Cars (id, make, model, n_cyl, hp) values (4, 'RAANDO3', 'BANDO3', 11, 18);
insert into Cars (id, make, model, n_cyl, hp) values (5, 'bad', 'bad', 6, 3);



SELECT 
  id,
  make,
  model,
  hp
FROM
  Cars
WHERE
  n_cyl > 6
ORDER BY hp DESC
LIMIT 3;





SELECT 
  id,
  make,
  model,
  hp
FROM
  Cars
WHERE
  n_cyl >= 6
  AND hp IN 
  (
    SELECT DISTINCT
      hp
    FROM
      Cars a
    WHERE
      a.n_cyl >= 6 AND
      3 > -- the number of distinct horsepowerse greateer than a.hp < 3 
      (SELECT
        COUNT(DISTINCT hp)
       FROM
         Cars b
        WHERE
          b.hp > a.hp AND b.n_cyl >= 6
      )
  )
  ;





SELECT
  *
  -- cars_a.*
FROM
  Cars cars_a
LEFT JOIN
  Cars cars_b ON cars_a.hp < cars_b.hp
WHERE
  cars_b.hp is NULL;
