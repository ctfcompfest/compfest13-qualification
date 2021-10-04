const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded({ extended: true }))

BLACKLIST = ['require', 'exec', 'eval', 'exec', 'module']
fL4g1sHeR3_jasdu2724 = function() {
    var whatYouNeed = "_dat4_i5_proHibiTed_14f07bc4bd}"
    whatYouNeed = "COMPFEST13{hARdcoDeD_senS1tiv3" + whatYouNeed
    return "Sorry, we wont return the flag"
}

function getHtml(res) {
    let html = "Enter expression: <form method='POST'><input type='text' name='expr' placeholder='1+2'/><input type='submit' value='submit'></form>"
    if (res !== undefined) html += "<br>" + res
    return html
}

function isCyclic (obj) {
    var seenObjects = [];
  
    function detect (obj) {
      if (obj && typeof obj === 'object') {
        if (seenObjects.indexOf(obj) !== -1) {
          return true;
        }
        seenObjects.push(obj);
        for (var key in obj) {
          if (obj.hasOwnProperty(key) && detect(obj[key])) {
            return true;
          }
        }
      }
      return false;
    }
  
    return detect(obj);
}

function consoleLogMode(val) {
    
    if (typeof val === 'function') return "[object function]"
    if (typeof val !== 'object') return val
    if (typeof val === 'object') {
        if (val instanceof String) return "[object string]"
        if (val instanceof Number) return "[object number]"
        if (val instanceof Array) return "[object array]"
        if (val instanceof Date) return "[object date]"
        if (val instanceof Map) return "[object map]"
        if (val instanceof WeakMap) return "[object weakmap]"
        if (val instanceof Set) return "[object set]"
        if (val instanceof WeakSet) return "[object weakset]"
    }

    let keys = Object.keys(val)
    let szKey = keys.length
    let ret = ""
    for (let i = 0; i < szKey; i++) {
        let k = keys[i]
        if (isCyclic(val[k])) continue
        ret += `${k}: ${consoleLogMode(val[k])}`
        if (i < szKey) ret += ", "
    }

    return ret
}

function validate(s) {
    let sz = BLACKLIST.length
    for (let i = 0; i < sz; i++) {
        if (s.includes(BLACKLIST[i]))
            return false
    }
    return true
}

app.post('/', function(request, response){
    let expr = request.body.expr
    if (expr === undefined || expr === "") {
        return response.send(getHtml())
    }
    if (!validate(expr)) {
        return response.send(getHtml('Stay away from hacking!'))
    }
    
    let evalRes = eval(expr)
    console.log(evalRes)
    return response.send(getHtml(consoleLogMode(evalRes)))
})

app.get('/', function(request, response){
    response.send(getHtml())
})

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`)
})