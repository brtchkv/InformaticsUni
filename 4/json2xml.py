def convert(json, line = " "):
    result = []

    json_type = type(json)

    if json_type is dict:
        for tag in json:
            sub_obj = json[tag]
            result.append("%s<%s>" % (line, tag))
            result.append(convert(sub_obj, "\t" + line))
            result.append("%s</%s>" % (line, tag))

        return "\n".join(result)

    return "%s%s" % (line, json)


with open("data.txt","r") as f:
    s = f.readlines()
    print(print('\n'+ "JSON:" + '\n'), eval(s[0]))
    f.close()

k = s[0]

d = eval(k)

print('\n'*2 + "XML:")

print(convert(d))

