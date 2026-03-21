
document.getElementById("burnoutForm").addEventListener("submit", function(e) {
    // e.preventDefault();

    // values lena
    let name = document.getElementById("name").value;
    let sleep = document.getElementById("sleep").value;
    let study = document.getElementById("study").value;
    let stress = document.getElementById("stress").value;
    let screen = document.getElementById("screen").value;

    // validation (simple)
    if(name === "" || sleep === "" || study === "" || stress === "" || screen === "") {
        alert("Please fill all details 😅");
        return;
    }

    // console output
    console.log("----- Burnout Data -----");
    console.log("Name:", name);
    console.log("Sleep Hours:", sleep);
    console.log("Study Hours:", study);
    console.log("Stress Level:", stress);
    console.log("Screen Time:", screen);
    console.log("------------------------");

    // friendly message
    alert("Hey " + name + ", your data is recorded 👍");
});
