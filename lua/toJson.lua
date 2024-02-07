function(array)
    local dkjson = require "dkjson"
    local str_json = dkjson.encode(array, { indent = true })
    print(str_json)
end