It's a blog engine project with several functions:

1. Create posts/tags 
2. Read posts/tags
3. Update posts/tags
4. Delete posts/tags
5. Search posts

For easy using blog has paginator and admin panel (it allows to manage posts). 

For steup and run the project you need:
1. Git clone
2. Build container: docker build --tag python-django .
3. Run the server using next command: docker run --publish 8000:8000 python-django 

Before create/update/delete some posts you have to create Django superuser and login https://your_url/admin.
After that the admin pannel will be able to use.
