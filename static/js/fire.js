// Initialize Cloud Firestore through Firebase
var db = firebase.firestore();



function storeData(){

    var name =1;// document.getElementById("name").value;
    var amount = 1;//document.getElementById("amount").value;
    var term = 1;//document.getElementById("term").value;
    var rate = 1;//document.getElementById("rate").value;
    var len = 1;//document.getElementById("len").value;
    var home = 1;//document.getElementById("home").value;
    var inc = 1;//document.getElementById("inc").value;
    var plan =1;// document.getElementById("plan").value;
    var purp = 1;//document.getElementById("purp").value;
    var dti = 1;//document.getElementById("dti").value;
    var pub = 1;//document.getElementById("pub").value;
    var rev = 1;//document.getElementById("rev").value;
    var util = 1;//document.getElementById("util").value;
    
    
    
        // Add a new document in collection "cities"
    db.collection("Loans").doc().set({
        name: name,
        amount: amount,
        term: term,
        rate: rate,
        len: len,
        home: home,
        inc: inc,
        plan: plan,
        purp: purp,
        dti: dti,
        pub: pub,
        rev: rev,
        util: util
    })
    .then(function() {
        console.log("Document successfully written!");
    })
    .catch(function(error) {
        console.error("Error writing document: ", error);
    });
}

const list_div = document.querySelector("#list_div");

db.collection("Loans").onSnapshot(function(querySnapshot) {
    querySnapshot.docChanges().forEach(function(change) {
        if(change.type === "added"){
            var text = list_div.innerHTML;
            if(change.doc.data().amount > 15) //if it is payed back use
                list_div.innerHTML =  "<a class='twitter btn'> To: " + change.doc.data().name + "<br><br>Amount: "  + change.doc.data().amount + " <br> <br>Term: " + change.doc.data().term +  "<br><br>Rate: "+ change.doc.data().rate+ "<br><br>Length: " +change.doc.data().len +  "<br><br>Home Ownership Status: "  + change.doc.data().home + "<br><br>Annual Income: "  + change.doc.data().inc + " <br> <br>Payment Plan: " + change.doc.data().plan +  "<br><br>Purpose Of Loan: "+ change.doc.data().purp+ "<br><br>DTI: " +change.doc.data().dti +  "<br><br>Derogatory Public Records: "  + change.doc.data().pub +   "<br><br> Total credit revolving balance: "  + change.doc.data().rev + "<br><br> Util: "  + change.doc.data().util +"<br> <br><b style='color: #000000'> Loan Will Be Payed Back</b></a>" + text;
            else{ //if it isnt payed back use this

                list_div.innerHTML =  "<a class='google btn'> To: " + change.doc.data().name + "<br><br>Amount: "  + change.doc.data().amount + " <br> <br>Term: " + change.doc.data().term +  "<br><br>Rate: "+ change.doc.data().rate+ "<br><br>Length: " +change.doc.data().len +  "<br><br>Home Ownership Status: "  + change.doc.data().home + "<br><br>Annual Income: "  + change.doc.data().inc + " <br> <br>Payment Plan: " + change.doc.data().plan +  "<br><br>Purpose Of Loan: "+ change.doc.data().purp+ "<br><br>DTI: " +change.doc.data().dti +  "<br><br>Derogatory Public Records: "  + change.doc.data().pub +  "<br><br> Total credit revolving balance: "  + change.doc.data().rev + "<br><br> Util: "  + change.doc.data().util +"<br> <br><b style='color: #000000'> Loan Will NOT Be Payed Back</b></a>" + text;
            }
        }
    });
});
//To: Mr. Scott DeRuiter<br><br>Taken: 06/25/18 <br> <br>Amount: $25,300,032<br> <br><b style="color: #000000"> Loan Will Be Payed Back</b>