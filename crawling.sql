show databases;

use movie;

show databases;
create database movie;
use movie;



create database movies;
use movies;

create table movies
  (
	 id int auto_increment primary key,	
     title  longtext,
     movie_rate longtext,
     netizen_rate float,
     netizen_count int ,
     journalist_score float,
     journalist_count int,
     scope longtext,
     playing_time longtext,
     opening_date longtext,
	 director longtext,
     image longtext,
     enter_date DATETIME DEFAULT NOW() );
 
show tables;
select * from movie;

   
  