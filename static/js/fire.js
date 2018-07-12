// Initialize Cloud Firestore through Firebase
var db = firebase.firestore();


db.collection("Loans").onSnapshot(function(querySnapshot) {
    querySnapshot.docChanges().forEach(function(change) {
        if(change.type === "added"){
            var text = list_div.innerHTML;
            if(3>4) //if it is payed back use
                list_div.innerHTML =  "<a class='twitter btn'> To: " + change.doc.data().name + "<br><br>Amount: "  + change.doc.data().amount + " <br> <br>Term: " + change.doc.data().term +  "<br><br>Rate: "+ change.doc.data().rate+ "<br><br>Length: " +change.doc.data().len +  "<br><br>Home Ownership Status: "  + change.doc.data().home + "<br><br>Annual Income: "  + change.doc.data().inc + " <br> <br>Payment Plan: " + change.doc.data().plan +  "<br><br>Purpose Of Loan: "+ change.doc.data().purp+ "<br><br>DTI: " +change.doc.data().dti +  "<br><br>Derogatory Public Records: "  + change.doc.data().pub +   "<br><br> Total credit revolving balance: "  + change.doc.data().rev + "<br><br> Util: "  + change.doc.data().util +"<br> <br><b style='color: #000000'> Loan Will Be Payed Back</b></a>" + text;
            else { //if it isnt payed back use this

                list_div.innerHTML = "<a class='google btn'> To: " + change.doc.data().name + "<br><br>Amount: "  + change.doc.data().amount + " <br> <br>Term: " + change.doc.data().term +  "<br><br>Rate: "+ change.doc.data().rate+ "<br><br>Length: " +change.doc.data().len +  "<br><br>Home Ownership Status: "  + change.doc.data().home + "<br><br>Annual Income: "  + change.doc.data().inc + " <br> <br>Payment Plan: " + change.doc.data().plan +  "<br><br>Purpose Of Loan: "+ change.doc.data().purp+ "<br><br>DTI: " +change.doc.data().dti +  "<br><br>Derogatory Public Records: "  + change.doc.data().pub +  "<br><br> Total credit revolving balance: "  + change.doc.data().rev + "<br><br> Util: "  + change.doc.data().util +"<br> <br><b style='color: #000000'> Loan Will NOT Be Payed Back</b></a>" + text;
            }
        }
    });
});