$.ajax({
    type: "GET",
    dataType: "json",
    url: "http://127.0.0.1:5000/get-articles",
    success: function (data) {
        buf1 = data;
        console.log("hhhhhhhhhhhhhhhhhhhhhhhh")
        console.log(data);
    }
})