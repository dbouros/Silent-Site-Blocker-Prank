from datetime import datetime, date

# linux Path to hosts
# hosts_path = "/etc/hosts"

# Windows Path to hosts
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"  # localhost ip address to redirect us so we can't log in to site

# The end time of the block will be year from the current date
block_end_time = datetime(date.today().year + 100, date.today().month, date.today().day)  # datetime(year, month, day, time)
sites_to_block = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com', 'www.google.com', 'google.com']

def block_sites():
    if datetime.now() < block_end_time:  # checks current time with the block_end_time given above
        print("Sites Blocked!")
        with open(hosts_path, 'r+') as hostsfile:  # opens hosts file from the path as read and write mode
            hosts_content = hostsfile.read()
            for site in sites_to_block:  # Loops the list sites_to_block[] with the 2 website names
                if site not in hosts_content:  # checks the site with what the file is being read from the file

                    hostsfile.write(redirect + " " + site + "\n")  # writes in hosts file the redirection of the site
                    # to our local ip so that we can't reach it

    else:
        print("Sites Unblocked!")
        with open(hosts_path, 'r+') as hostsfile:  # r+ == read and write permission
            lines = hostsfile.readlines()  # reads the lines from the path file
            hostsfile.seek(0)  # seeks the pointer to the beginning of the file
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    # if the current line that is read from the hosts file is not equal with the sites_to_block then you
                    # rewrite that line as it is back in the file
                    hostsfile.write(line)
                else:
                    # if line == sites_to_block , then you delete that whole line, which will make the site unblocked again
                    hostsfile.truncate()


block_sites()
