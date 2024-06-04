$(document).ready(function () {
    var url = "http://127.0.0.1:8000/apiV1/todo/list/"
    fetch(url, {
        method: 'GET'
        //    body:JSON.stringify({'post_data':Data to post}) //JavaScript object of data to POST
    })
        .then((resp) => resp.json())
        .then((data) => {
            console.log('data:', data)
            
            for (let i = 0; i < data['length']; i++) {
                const tr = document.createElement("tr");
                const para = document.createElement("td");
                para.innerText = data[0].title;
                document.body.appendChild(para);
                document.body.insertBefore(newDiv, currentDiv);
            }
        });
});