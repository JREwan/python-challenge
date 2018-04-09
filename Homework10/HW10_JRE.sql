#  Homework 10 - SQL
#  submitted by John Ewan
#
#  NOTES to those grading - Apologies, but I don't capitalize SQL keywords - type too slow as it is!
#                         - thanks for understanding!
#
use sakila;

# 1a. Display the first and last names of all actors from the table actor;

select first_name, last_name from actor;

# 1b. Display the first and last name of each actor in a single column in 
#     upper case letters. Name the column Actor Name;

select concat_ws(" ", first_name, last_name) as Actor_Name 
   from actor;

# 2a. You need to find the ID number, first name, and last name of an actor,
#     of whom you know only the first name, "Joe." What is one query would 
#     you use to obtain this information?

select actor_id, first_name, last_name 
   from actor
   where first_name = "JOE";

# 2b. Find all actors whose last name contain the letters GEN:

select actor_id, first_name, last_name 
   from actor
   where last_name like "%GEN%";

# 2c. Find all actors whose last names contain the letters LI. This time, 
#     order the rows by last name and first name, in that order

select last_name, first_name, actor_id 
   from actor
   where last_name like "%LI%"
   order by last_name asc, first_name asc;

# 2d. Using IN, display the country_id and country columns of the following
#     countries: Afghanistan, Bangladesh, and China:

select country_id, country
   from country
   where country in ("Afghanistan", "Bangladesh", "China");

# 3a. Add a middle_name column to the table actor. Position it between 
#     first_name and last_name. Hint: you will need to specify the data type

alter table actor
   add column middle_name varchar(15)
   after first_name;

# 3b. You realize that some of these actors have tremendously long last names.
#     Change the data type of the middle_name column to blobs.

describe actor;

alter table actor 
   change middle_name middle_name blob;

# 3c. Now delete the middle_name column.

describe actor;

alter table actor drop column middle_name;

# 4a. List the last names of actors, as well as how many actors have that last name.

select last_name, count(last_name) as occurances
   from actor
   group by last_name;

# 4b. List last names of actors and the number of actors who have that last name,
#     but only for names that are shared by at least two actors

select a.last_name, count(a.last_name) as occurs
   from actor as a
   group by a.last_name
   having count(a.last_name) > 1;
      

# 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as 
#     GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher.
#     Write a query to fix the record.

describe actor;

select * 
   from actor
   where first_name = "GROUCHO";

update actor
   set first_name = "HARPO"
   where actor_id = 172;

select * 
   from actor    
   where actor_id = 172;

# 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO
#     was the correct name after all! In a single query, if the first name of the actor
#     is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO
#     GROUCHO, as that is exactly what the actor will be with the grievous error.
#
# BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! 
#     (Hint: update the record using a unique identifier.)

select * 
   from actor
   where actor_id = 172;

update actor 
   set first_name = case
                    when first_name = "HARPO" then "GROUCHO" 
                    when first_name != "HARPO" then "MUCHO GROUCHO"
                    end
      where actor_id = 172;
      


# 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
#     Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html

show create table actor;

# 6a. Use JOIN to display the first and last names, as well as the address, of each staff member.
#     Use the tables staff and address

describe staff;

select * from staff;

describe address;

select staff.first_name, staff.last_name, address.address, address.address2
   from staff
   inner join address on
      staff.address_id = address.address_id;
          
     
# 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use
#     tables staff and payment

describe staff;

select * from staff;

describe payment;

select count(*) from payment;

select staff.staff_id, staff.first_name, staff.last_name, sum(payment.amount) as rung_up
   from staff
   left outer join payment 
   on staff.staff_id = payment.staff_id
   where payment.payment_date like "2005-08%"
   group by staff.staff_id;
   

# 6c. List each film and the number of actors who are listed for that film. Use tables film_actor 
#     and film. Use inner join

desc film_actor;

select fa.film_id, film.title, count(fa.actor_id) as actor_count
   from film_actor as fa
   inner join film
   on fa.film_id = film.film_id
   group by fa.film_id;

# 6d. How many copies of the film Hunchback Impossible exist in the inventory system?

desc inventory;

select * from inventory;

select * from film where title = "Hunchback Impossible";

select film_id, count(film_id)
  from inventory
  where film_id = (select film_id 
                   from film
                   where title = "Hunchback Impossible"
                   );

# 6e. Using the tables payment and customer and the JOIN command, list the total paid by
#     each customer. List the customers alphabetically by last name:

desc payment;

select p.customer_id, c.first_name, c.last_name, sum(p.amount)
   from payment as p
   inner join customer as c
      on p.customer_id = c.customer_id
   group by p.customer_id
   order by c.last_name;

# 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an 
#     unintended consequence, films starting with the letters K and Q have also soared in
#     popularity. Use subqueries to display the titles of movies starting with the letters
#     K and Q whose language is English.

select * from language;

select f.title 
   from film as f
   where f.title like "K%"
      or f.title like "Q%"
      and f.language_id = (select l.language_id 
                              from language as l
                              where l.name = "English"
                              );

# 7b. Use subqueries to display all actors who appear in the film Alone Trip.

select * from film where title = "Alone Trip";

select * from film_actor where film_id = 17;

select * from actor where actor_id in (3, 12, 13, 82, 100, 160, 167, 187);

select a.first_name, a.last_name
   from actor as a
   where a.actor_id in (select fa.actor_id
                           from film_actor as fa
                           where fa.film_id = (select f.film_id 
                              from film as f 
                              where f.title = "Alone Trip")
                           );
                           

# 7c. You want to run an email marketing campaign in Canada, for which you will
#     need the names and email addresses of all Canadian customers. Use joins to
#     retrieve this information.

desc customer;

select * 
   from country
   where country = "Canada";

select city_id 
   from city 
   inner join country
   on city.country_id = country.country_id
   where country.country = "Canada";

select c.first_name, c.last_name, c.email
   from customer as c
   inner join address as a 
   on c.address_id = a.address_id
   where a.city_id in (select city_id 
                       from city 
                       inner join country
                       on city.country_id = country.country_id
                       where country.country = "Canada"
                       );


# 7d. Sales have been lagging among young families, and you wish to target all 
#     family movies for a promotion. Identify all movies categorized as famiy films.

select * from category;

select f.title as Family_Films
   from film as f
   where f.film_id in (select fc.film_id 
                          from film_category as fc
                          where fc.category_id = (select c.category_id 
                                                     from category as c
                                                     where c.name = "Family"));


# 7e. Display the most frequently rented movies in descending order.
desc rental;

select count(distinct(inventory_id)) from rental; 

select i.film_id, f.title, r.inventory_id, count(r.inventory_id) as rented
   from rental as r
   inner join inventory as i
   on r.inventory_id = i.inventory_id 
   inner join film as f
   on i.film_id = f.film_id
   group by r.inventory_id
   order by count(r.inventory_id) desc;
   

# 7f. Write a query to display how much business, in dollars, each store brought in.
desc store;
desc payment;
desc rental;
desc inventory;
select * from store;

select s.store_id, sum(p.amount) as revenue
   from store as s
   inner join inventory as i
   on s.store_id = i.store_id
   inner join rental as r
   on i.inventory_id = r.inventory_id
   inner join payment as p
   on r.rental_id = p.rental_id
   group by s.store_id;

# 7g. Write a query to display for each store its store ID, city, and country.
desc store;
select * from store;

select s.store_id, city.city, c.country
   from store as s
   inner join address as a
   on s.address_id = a.address_id
   inner join city
   on a.city_id = city.city_id
   inner join country as c
   on city.country_id = c.country_id
   ;
   
# 7h. List the top five genres in gross revenue in descending order. (Hint: you 
#     may need to use the following tables: category, film_category, inventory, 
#     payment, and rental.)
desc category;
desc film_category;
desc inventory;
desc payment;
desc rental;

select * from category;

select cat.name, sum(p.amount) as gross_revenue
   from category as cat
   inner join film_category as fc
   on cat.category_id = fc.category_id
   inner join inventory as i
   on fc.film_id = i.film_id
   inner join rental as r
   on i.inventory_id = r.inventory_id
   inner join payment as p
   on r.rental_id = p.rental_id
   group by cat.name 
   order by sum(p.amount) desc limit 5
   ;


# 8a. In your new role as an executive, you would like to have an easy way of viewing
#     the Top five genres by gross revenue. Use the solution from the problem above to
#     create a view. If you haven't solved 7h, you can substitute another query to create a view.
create view top_5_genres_view as 
   select cat.name, sum(p.amount) as gross_revenue
   from category as cat
   inner join film_category as fc
   on cat.category_id = fc.category_id
   inner join inventory as i
   on fc.film_id = i.film_id
   inner join rental as r
   on i.inventory_id = r.inventory_id
   inner join payment as p
   on r.rental_id = p.rental_id
   group by cat.name 
   order by sum(p.amount) desc limit 5
   ;


# 8b. How would you display the view that you created in 8a?
select * from top_5_genres_view;

# 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
Drop view  if exists top_5_genres_view;
