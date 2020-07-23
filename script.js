var queryData = {}
queryData['search_word'] = '웰시코기'
queryData['total_cnt'] = 50
queryData['Dir'] = "D:/rain/image-crawler/img/"

$.ajax({
    type:"POST",
    url: "./crawler.py",
    data: {param: queryData}
}).done(function(){
    console.log("success");
})