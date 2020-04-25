from locust import HttpLocust, TaskSet, TaskSequence, between, task


class UserBehavior(TaskSet):

    # a "setUp()" function of sorts
    def on_start(self):

        """ on_start is called when a Locust start before any task is scheduled """

        # possible setUp operation??
        # self.client.post("/login", {"username":"admin", "password":"admin"})
        pass

    # a "tearDown()" function of sorts
    def on_stop(self):

        """ on_stop is called when the TaskSet is stopping """

        # possible tearDown operation??
        # self.client.post("/logout", {"username":"admin", "password":"admin"})
        pass

    # this function with the @task decorator defines the UserBehaviour class
    @task
    def get_livelog(self):
        self.client.get("/livelog")


# class UserBehavior2(TaskSet):

#     # @task takes an optional "weight" argument that can be used to specify the task’s execution ratio,
#     # so here get_livelog2 will be executed twice as much as get_livelog1

#     @task(2) 
#     def get_livelog2(self):
#         self.client.get("/livelog")

#     @task(1)
#     def get_livelog1(self):
#         self.client.get("/livelog")


# class UserBehavior3(TaskSequence):

#     # @seq_task(number) indicates order in which tasks to a TaskSequence class are executed

#     @seq_task(1)
#     def get_livelog1(self):
#         self.client.get("/livelog")

#     @seq_task(2) 
#     def get_livelog2(self):
#         self.client.get("/livelog")


class WebsiteUser(HttpLocust):

    # what this WebsiteUser is going to be doing
    task_set = UserBehavior

    # random time between user's requests
    wait_time = between(1.0, 3.0)