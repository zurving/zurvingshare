var timeout = null;

function pageReady(){
    $(".sharesimage").click( showShares );
    $(".statsimage").click( showStatus );
    showStatus();
}

function showShares(){
    if( timeout != null ){
        clearTimeout( timeout );
    }
    $.get( '/z/shares/', {}, displayShares );
}

function displayShares( data ) {
    $("#content").remove();
    var docWidth = $( document ).width();
    var ct = $("<div id=\"content\"/>");
    if( docWidth > 600 ){
        ct.css("width","600px").css("margin-left", "-300px").css("font-size", "3em").css("height", "900px");
    }else{
        ct.css("width","300px").css("margin-left", "-150px").css("height", "450px");
    }
    for( var i=0; i < data.shares.length; i++ ){
        var ld = $("<div/>").addClass("columncontent").html( "hello, world")
        ld.css( "grid-column-start", 1 ).css("grid-column-end", 1);
        ld.css( "grid-row-start", i+1 ).css( "grid-row-end", i+1 );
        ct.append( ld );    
    }
    $('body').append( ct );
}

function showStatus(){
    $.get( '/z/status/', {}, displayStatus )
}

function displayStatus( data ){
    $("#content").remove();
    var docWidth = $( document ).width();
    var ct = $("<div id=\"content\"/>");
    if( docWidth > 600 ){
        ct.css("width","600px").css("margin-left", "-300px").css("font-size", "3em").css("height", "900px");
    }else{
        ct.css("width","300px").css("margin-left", "-150px").css("height", "450px");
    }
    var ld = $("<div/>").addClass("gridcontent").addClass( 'load' ).html( 'load<br/>' + Math.round(data.load*100)/100 );
    ct.append( ld );
    var temp = $("<div/>").addClass("gridcontent").addClass( 'cpu_temp' ).html( 'temp<br/>' + Math.round( data.temp ) );
    ct.append( temp );
    var mem = $("<div/>").addClass("gridcontent").addClass( 'memory' ).html( 'mem<br/>' + Math.round(data.memory) );
    ct.append( mem );
    var desc = $("<div/>").addClass("gridcontent").addClass( 'desc' ).html( 'stats' );
    ct.append( desc );
    var up = $("<div/>").addClass("gridcontent").addClass( 'upload' ).html( 'up<br/>' + data.upload );
    ct.append( up );
    var down = $("<div/>").addClass("gridcontent").addClass( 'download' ).html( 'down<br/>' + data.download );
    ct.append( down );
    $('body').append( ct );
    timeout = setTimeout( showStatus, 15000 );
}

$( document ).ready( pageReady );