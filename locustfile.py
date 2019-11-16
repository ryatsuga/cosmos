from locust import HttpLocust, TaskSet, task

class UserActions(TaskSet):

	def on_start(self):
		self.login()

	def login(self):
		# Logar no site
		response = self.client.get('login/')
		csrftoken = response.cookies['csrftoken']
		self.client.post('login/',
						 {'username': 'username', 'password': 'password'}, 
						 headers={'X-CSRFToken': csrftoken})

class ApplicationUser(HttpLocust):
	task_set = UserActions
	min_wait = 0
	max_wait = 0
