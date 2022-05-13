show databases;

use movie;

create table movie
  (
     title varchar(30) ,
     movie_rate varchar(20),
     netizen_rate float (4),
     netizen_count int (10),
     journalist_score float(4),
     journalist_count int(10),
     scope varchar(30),
     playing_time varchar(10),
     opening_date varchar(20),
	 director varchar(30),
     image varchar(70)
     );

   
  