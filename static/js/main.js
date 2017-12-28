
        function GetQueryString(name)
        {
             var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
             var r = window.location.search.substr(1).match(reg);
             if(r!=null)return  decodeURI(r[2]); return null;
        }

        var tag = '';
        // 分页点击查询
        $('#callBackPager').extendPagination({
                  totalCount:9,
                  showCount:3,
                  limit:6,
                  callback:function(curr,limit,total){
                      createTable(curr,limit,total);
                 }
        });

        function createTable(currPage, limit, total) {

            var arr = [], showNum = limit;

            if (total - (currPage * limit) < 0) showNum = total - ((currPage - 1) * limit);

            $.get('/queryArticle',{tag:tag, currPage:currPage},function(d){

                 var data = $.parseJSON(d);
                 reloadArticle(data);

           });
       }

        //分类查询下 执行的分页查询
        function segmentPage(length) {
          $('#callBackPager').extendPagination({
            totalCount:length,
            showCount:3,
            limit:6,
            callback:function(curr,limit,total){
              createTable(curr,limit,total);
            }
          });
        }

        //类别查询
      $('.category').click(function () {

          tag = $(this).children('.tag').text();

          tag = $.trim(tag);//去前后空格

          alert('tag=' + tag);

          queryTag(tag);


       });




      function reloadArticle(data) {

             var mainObj = $('.subText');

              mainObj.empty();

              for(var i = 0; i < data.length; i++){
                    // var tmp  = new Date(data[i].time);
                    // var time = tmp.getFullYear() + '-' + (tmp.getMonth()+1) +'-' + tmp.getDate() + ' ' + tmp.getHours() + ':' + tmp.getMinutes() +':'+tmp.getSeconds();
                     $('.subText').append('<div class="col-xs-12 col-sm-12 col-lg-12 home_subArticle" id='+data[i].id+'>'+
                    '<div class="thumbnail">'+
                    '<div class="caption"><span class="label label-success btn">'+data[i].tag+'</span><span class="time-label">'+data[i].time+'</span>'+
                     '<h2>'+data[i].title+'</h2>'+
                    '<p class="main-sub-content">'+data[i].desc+'</p>'+
                     '<p> <button class="btn btn-primary readAll" role="button">阅读全文</button></p>'+
                    '</div></div></div>');
              }


      }


      function queryTag(tag){

          $.get('/queryTag',{tag:tag},function (d) {

              var data = $.parseJSON(d);
              var rData;
              if(data.length > 6)
                 rData = data.slice(0,6);
              else
                 rData = data;

              reloadArticle(rData);

              segmentPage(data.length);

          });
      }

      function queryTag_read(tag){

          $.get('/queryTag',{tag:tag},function (d) {

              var data = $.parseJSON(d);
//              var rData;
//              if(data.length > 6)
//                 rData = data.slice(0,6);
//              else
//                 rData = data;
//
//              reloadArticle(rData);

              segmentPage(data.length);

          });
      }

      $(document).ready(function () {
         tag = GetQueryString('tag');

         queryTag_read(tag);

      });

      $(document).on("click","button",function () {

          var myId = $(this).parents(".home_subArticle").attr('id');

          $.get('/queryCID', {id:myId}, function(d){

                var data = $.parseJSON(d);

                location.href = "/article?tag="+tag+"&id="+myId+"&cid="+data.cid;


          });



      });
