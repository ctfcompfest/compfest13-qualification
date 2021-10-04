const puppeteer = require('puppeteer-core')

const DOMAIN = process.env.HOST || "http://localhost:8000"
const USERNAME = process.env.ACC_USERNAME || "richGuy"
const PASSWORD = process.env.ACC_PASSWORD || "IniPasswordAmanGakMungkinKetahuan13"

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
  
const open_url = async (url, page, fn = null) => {
    try {
        if (page == undefined)
            page = await browser.newPage()
        
        await page.on('error', err => {
            //console.error(`[#] Error!`, err)
        })

        await page.on('pageerror', msg => {
            //console.error(`[-] Page error : `, msg)
        })

        await page.on('dialog', async dialog => {
            //console.debug(`[#] Dialog : [${dialog.type()}] "${dialog.message()}" ${dialog.defaultValue() || ""}`)
            await dialog.dismiss()
        })

        await page.on('console', async msg => {
            msg.args().forEach(arg => {
                arg.jsonValue().then(_arg => {
                    //console.log(`[$] Console : `, _arg)
                })
            })
        })

        await page.on('requestfailed', req => {
            //console.error(`[-] Request failed : ${req.url()} ${req.failure().errorText}`)
        })

        await page.goto(url, {
            waitUntil: 'networkidle0',
        })
    
        if (fn != null)
            await fn(page)
    } catch (e) {
        //console.error("[-] Page open_url\n", e.stack)
    }
}

const login_page_function = async(page) => {
    await page.type('#inputUsername', USERNAME)
    await page.type('#inputPassword', PASSWORD)
    await page.click('#btn-login')
    await page.waitForNavigation()
}

var browser
(async () => {
    browser = await puppeteer.launch({
        executablePath: '/usr/bin/chromium-browser',
        args: [
            '--headless',
            '--disable-dev-shm-usage',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-gpu',
            '--no-gpu',
            '--disable-default-apps',
            '--disable-translate',
            '--disable-device-discovery-notifications',
            '--disable-software-rasterizer',
            '--disable-xss-auditor'
        ],
        userDataDir: '/home/bot/data/',
        ignoreHTTPSErrors: true
    })

    console.log("[+] Browser", "Launch success!")
    await sleep(10000)
    
    let page
    try {
        await open_url(DOMAIN + '/login', page, login_page_function)
        console.log("[+] Page", "Login success!")
        
        console.log('[+] Page', 'Starting to access received page')
        while (true) {
            await open_url(DOMAIN + '/history/received', page)
            await sleep(5000)
        }
    } catch {
        await page.close()
        console.log("[+] Page", "Close success!")
    } 

    await browser.close()
    console.log("[+] Browser", "Close success!")
})()