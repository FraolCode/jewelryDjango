$(document).ready(function () {

    function setcookie() {
        var cokname = 'cookie_ue';
        var cookiexne = '1';
        var expire = new Date();
        expire.setMonth(expire.getMonth() + 12);
        document.cookie = cokname + "=" + escape(cookiexne) + ";path=/;" + ((expire == null) ? "" : ("; expires=" + expire.toGMTString()))
    }

    $("#closenotification").click(function(){
                $('#ttcookie-outer').animate(
                    {bottom: '-250px'},
                   2500, function () {
                        $('#ttcookie-outer').hide();
                    });
            setcookie();
    });
});
