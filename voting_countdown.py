from rumps import rumps
from datetime import datetime, timedelta, date # temporal objects
import os

icon_path = "data/election.png"

class voting(object):
	def __init__(self):
		self.icon_path = "data/election.png"
		self.app = rumps.App("voting", icon=icon_path)
		#updated hourly
		self.timer = rumps.Timer(self.ticker, 600) 
 
		self.time_till_election = rumps.MenuItem(title='placeholder')
		self.app.menu = [self.time_till_election, 
			None,
			rumps.MenuItem("Am I registred to vote?"),
			None, 
			rumps.MenuItem("Register to Vote"),
			None,
			rumps.MenuItem("Register to Vote by Mail"),
			None, 
			rumps.MenuItem("Get Nearest Polling Location"),
			None,
			[rumps.MenuItem(title='ID Requirements (by State)', dimensions=(16,16)), 
			[
				rumps.MenuItem('Alabama'),
				rumps.MenuItem('Alaska'),
				rumps.MenuItem('Arizona'),
				rumps.MenuItem('Arkansas'),
				rumps.MenuItem('California'),
				rumps.MenuItem('Colorado'),
				rumps.MenuItem('Connecticut'),
				rumps.MenuItem('Delaware'),
				rumps.MenuItem('District of Columbia'),
				rumps.MenuItem('Florida'),
				rumps.MenuItem('Georgia'),
				rumps.MenuItem('Hawaii'),
				rumps.MenuItem('Idaho'),
				rumps.MenuItem('Illinois'),
				rumps.MenuItem('Indiana'),
				rumps.MenuItem('Iowa'),
				rumps.MenuItem('Kansas'),
				rumps.MenuItem('Kentucky'),
				rumps.MenuItem('Louisiana'),
				rumps.MenuItem('Maine'),
				rumps.MenuItem('Maryland'),
				rumps.MenuItem('Massachusetts'),
				rumps.MenuItem('Michigan'),
				rumps.MenuItem('Minnesota'),
				rumps.MenuItem('Mississippi'),
				rumps.MenuItem('Missouri'),
				rumps.MenuItem('Montana'),
				rumps.MenuItem('Nebraska'),
				rumps.MenuItem('Nevada'),
				rumps.MenuItem('New Hampshire'),
				rumps.MenuItem('New Jersey'),
				rumps.MenuItem('New Mexico'),
				rumps.MenuItem('New York'),
				rumps.MenuItem('North Carolina'),
				rumps.MenuItem('North Dakota'),
				rumps.MenuItem('Ohio'),
				rumps.MenuItem('Oklahoma'),
				rumps.MenuItem('Oregon'),
				rumps.MenuItem('Pennsylvania'),
				rumps.MenuItem('Rhode Island'),
				rumps.MenuItem('South Carolina'),
				rumps.MenuItem('South Dakota'),
				rumps.MenuItem('Tennessee'),
				rumps.MenuItem('Texas'),
				rumps.MenuItem('Utah'),
				rumps.MenuItem('Vermont'),
				rumps.MenuItem('Virginia'),
				rumps.MenuItem('Washington'),
				rumps.MenuItem('West Virginia'),
				rumps.MenuItem('Wisconsin'),
				rumps.MenuItem('Wyoming')
			]],
			None,
			rumps.MenuItem("About Vote.org"),
			None,
			rumps.MenuItem("About 2020 Voting Countdown"),
		]
		self.timer.count = datetime.now()
		self.timer.end = datetime.strptime('2020-11-03 00:00:00', '%Y-%m-%d %H:%M:%S')
		self.timer.start()

	def ticker(self, dt):
		delta = dt.end - dt.count
		days, seconds = delta.days, delta.seconds
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60
		if days <= 0:
			self.app.title = 'Today!'
			self.time_till_election.title = 'Today is election day!'
		else:
			self.time_till_election.title = f'{days} days, {hours} hours until 2020 Election'
			self.app.title = f'{days}'
		dt.count += timedelta(seconds=600)  

	@rumps.clicked("About Vote.org")
	def general(sender):
		os.system("open \"\" https://www.vote.org/about/")

	@rumps.clicked("Am I registred to vote?")
	def register_checker(sender):
		os.system("open \"\" https://www.vote.org/am-i-registered-to-vote/")

	@rumps.clicked("Register to Vote")
	def to_register(sender):
		os.system("open \"\" https://www.vote.org/register-to-vote/")

	@rumps.clicked("Register to Vote by Mail")
	def mailin(sender):
		os.system("open \"\" https://www.vote.org/absentee-ballot/")

	@rumps.clicked("Get Nearest Polling Location")
	def polling(sender):
		os.system("open \"\" https://www.vote.org/polling-place-locator/")

	@rumps.clicked("About 2020 Voting Countdown")
	def aboutButton(sender):
		rumps.Window(title="2020 Voting Countdown by Stephen Hsu", 
			message="Thanks for using Voting Countdown! \nVersion 1.0.0 \n \n \nGithub Source Code can be found at: \n \nhttps://github.com/stephenjhsu/voting_countdown_app \n \n \nIcon Credits: https://www.flaticon.com/authors/freepik \n \n \nView more at: https://inspireai.io/", 
			icon_path=icon_path).run()

	@rumps.clicked("ID Requirements (by State)", "Alabama")
	def alabama(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#alabama") 

	@rumps.clicked("ID Requirements (by State)", "Alaska")
	def alaska(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#alaska") 

	@rumps.clicked("ID Requirements (by State)", "Arizona")
	def arizona(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#arizona") 

	@rumps.clicked("ID Requirements (by State)", "Arkansas")
	def arkansas(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#arkansas") 

	@rumps.clicked("ID Requirements (by State)", "California")
	def california(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#california") 

	@rumps.clicked("ID Requirements (by State)", "Colorado")
	def colorado(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#colorado") 

	@rumps.clicked("ID Requirements (by State)", "Connecticut")
	def connecticut(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#connecticut") 

	@rumps.clicked("ID Requirements (by State)", "Delaware")
	def delaware(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#delaware") 

	@rumps.clicked("ID Requirements (by State)", "District of Columbia")
	def district_of_columbia(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#district-of-columbia") 

	@rumps.clicked("ID Requirements (by State)", "Florida")
	def florida(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#florida") 

	@rumps.clicked("ID Requirements (by State)", "Georgia")
	def georgia(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#georgia") 

	@rumps.clicked("ID Requirements (by State)", "Hawaii")
	def hawaii(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#hawaii") 

	@rumps.clicked("ID Requirements (by State)", "Idaho")
	def idaho(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#idaho") 

	@rumps.clicked("ID Requirements (by State)", "Illinois")
	def illinois(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#illinois") 

	@rumps.clicked("ID Requirements (by State)", "Indiana")
	def indiana(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#indiana") 

	@rumps.clicked("ID Requirements (by State)", "Iowa")
	def iowa(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#iowa") 

	@rumps.clicked("ID Requirements (by State)", "Kansas")
	def kansas(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#kansas") 

	@rumps.clicked("ID Requirements (by State)", "Kentucky")
	def kentucky(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#kentucky") 

	@rumps.clicked("ID Requirements (by State)", "Louisiana")
	def louisiana(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#louisiana") 

	@rumps.clicked("ID Requirements (by State)", "Maine")
	def maine(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#maine") 

	@rumps.clicked("ID Requirements (by State)", "Maryland")
	def maryland(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#maryland") 

	@rumps.clicked("ID Requirements (by State)", "Massachusetts")
	def massachusetts(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#massachusetts") 

	@rumps.clicked("ID Requirements (by State)", "Michigan")
	def michigan(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#michigan") 

	@rumps.clicked("ID Requirements (by State)", "Minnesota")
	def minnesota(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#minnesota") 

	@rumps.clicked("ID Requirements (by State)", "Mississippi")
	def mississippi(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#mississippi") 

	@rumps.clicked("ID Requirements (by State)", "Missouri")
	def missouri(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#missouri") 

	@rumps.clicked("ID Requirements (by State)", "Montana")
	def montana(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#montana") 

	@rumps.clicked("ID Requirements (by State)", "Nebraska")
	def nebraska(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#nebraska") 

	@rumps.clicked("ID Requirements (by State)", "Nevada")
	def nevada(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#nevada") 

	@rumps.clicked("ID Requirements (by State)", "New Hampshire")
	def new_hampshire(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#new-hampshire") 

	@rumps.clicked("ID Requirements (by State)", "New Jersey")
	def new_jersey(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#new-jersey") 

	@rumps.clicked("ID Requirements (by State)", "New Mexico")
	def new_mexico(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#new-mexico") 

	@rumps.clicked("ID Requirements (by State)", "New York")
	def new_york(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#new-york") 

	@rumps.clicked("ID Requirements (by State)", "North Carolina")
	def north_carolina(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#north-carolina") 

	@rumps.clicked("ID Requirements (by State)", "North Dakota")
	def north_dakota(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#north-dakota") 

	@rumps.clicked("ID Requirements (by State)", "Ohio")
	def ohio(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#ohio") 

	@rumps.clicked("ID Requirements (by State)", "Oklahoma")
	def oklahoma(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#oklahoma") 

	@rumps.clicked("ID Requirements (by State)", "Oregon")
	def oregon(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#oregon") 

	@rumps.clicked("ID Requirements (by State)", "Pennsylvania")
	def pennsylvania(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#pennsylvania") 

	@rumps.clicked("ID Requirements (by State)", "Rhode Island")
	def rhode_island(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#rhode-island") 

	@rumps.clicked("ID Requirements (by State)", "South Carolina")
	def south_carolina(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#south-carolina") 

	@rumps.clicked("ID Requirements (by State)", "South Dakota")
	def south_dakota(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#south-dakota") 

	@rumps.clicked("ID Requirements (by State)", "Tennessee")
	def tennessee(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#tennessee") 

	@rumps.clicked("ID Requirements (by State)", "Texas")
	def texas(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#texas") 

	@rumps.clicked("ID Requirements (by State)", "Utah")
	def utah(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#utah") 

	@rumps.clicked("ID Requirements (by State)", "Vermont")
	def vermont(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#vermont") 

	@rumps.clicked("ID Requirements (by State)", "Virginia")
	def virginia(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#virginia") 

	@rumps.clicked("ID Requirements (by State)", "Washington")
	def washington(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#washington") 

	@rumps.clicked("ID Requirements (by State)", "West Virginia")
	def west_virginia(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#west-virginia") 

	@rumps.clicked("ID Requirements (by State)", "Wisconsin")
	def wisconsin(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#wisconsin") 

	@rumps.clicked("ID Requirements (by State)", "Wyoming")
	def wyoming(self): 
	     os.system("open \"\" https://www.vote.org/voter-id-laws/#wyoming") 

	def run(self):
		self.app.run()

if __name__ == '__main__':
	app = voting()
	app.run()