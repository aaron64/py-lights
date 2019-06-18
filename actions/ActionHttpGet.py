from actions.Action import Action

import requests

###
# ActionHttpGet: triggers a get http request on trigger
###
class ActionHttpGet(Action):
	def __init__(self, params, url):
		super(ActionHttpGet, self).__init__(params, "HTTP Get")
		self.parameters["URL"] = url

	def trigger(self, params, val):
		r = requests.get(self.parameters["URL"])
		print("Http get response: {}".format(r.status_code))
