$("#quote_one").click(
    function() {
        $.get("quote", function(data) {
            $("#output").html(data);
            }
         )
     }
);

$("#quote_multi").click(
    function() {
        if ($("#number").val() > 0) {
            url = "quote/" + $("#number").val();
            $.get(url, function(data) {
                $("#output").html(data);
                }
            )
        } else {
            $("#output").html("<br><strong style='color:red;'>Please enter a number greater than 0</strong><br>");
        }
     }
);

$("#db_quotes").click(
    function() {
        $.get("mongo/get_all", function(data) {
            $("#output").html(data);
            }
         )
     }
);