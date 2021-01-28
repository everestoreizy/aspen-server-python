function UpdateFromLMS(){
    alert("Update from LMS");
    request({method: "GET", url: "/update_calendar"})
        .then(data => {
            console.log(data);
            document.location.reload();
        })
        .catch(error => {
            console.log("Error: " + error);
        });
}