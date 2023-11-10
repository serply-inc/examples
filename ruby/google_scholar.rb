require 'uri'
require 'net/http'
require 'openssl'

url = URI("https://api.serply.io/v1/scholar/q=machine+learning+research")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
http.verify_mode = OpenSSL::SSL::VERIFY_NONE

request = Net::HTTP::Get.new(url)
request["User-Agent"] = 'insomnia/8.4.0'
request["apikey"] = ENV["API_KEY"]

response = http.request(request)
puts response.read_body
