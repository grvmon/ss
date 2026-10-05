const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require("fs");

const html = fs.readFileSync("index.html", "utf-8");
const dom = new JSDOM(html, { runScripts: "dangerously", resources: "usable" });

dom.window.addEventListener("error", (event) => {
  console.error("JSDOM Error:", event.error);
});

setTimeout(() => {
  console.log("Advisor floating unit exists?", !!dom.window.document.getElementById("advisorFloatingUnit"));
}, 1000);
