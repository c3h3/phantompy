
page = require("webpage").create()

console.log 'The default user agent is ' + page.settings.userAgent

page.settings.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'

fs = require 'fs'

args = require('system').args
req_url = args[1]
res_file_path = args[2]


page.open req_url, (status) ->
	if status == "success"
		fs.write res_file_path, page.content, "w"
		console.log "SUCCESS"
	else
		console.log "FAIL"

	phantom.exit()