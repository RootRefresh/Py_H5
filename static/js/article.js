        function GetQueryString(name)
        {
             var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
             var r = window.location.search.substr(1).match(reg);
             if(r!=null)return  decodeURI(r[2]); return null;
        }

        var tag = GetQueryString('tag');
        var myID = GetQueryString('id');
        var myCID = GetQueryString('cid');

        console.log(tag)

        var currentIndex ;

        if(tag != 'null'){

            currentIndex = parseInt(myCID);

        }else{

            currentIndex = parseInt(myID);
        }


        $('.category').click(function () {

          tag = $(this).children('.tag').text();

          tag = $.trim(tag);

          location.href = "/?tag="+tag;

//          $.get('/queryTag',{tag:tag},function (d) {
//
//              var data = $.parseJSON(d);
//
//              segmentPage(data.length);




//          });

       });

       $('.pre').click(function () {

            currentIndex--;
            paging(0);

       });

       $('.next').click(function () {
            currentIndex++;
            paging(1);

       });


       function paging(isNext){

         $.get('/articlePaging',{tag:tag, id:myID, cid:myCID, next:isNext, index:currentIndex},function (d) {

               if (d==''){
                   if(isNext==1)
                     --currentIndex;
                   else
                       ++currentIndex;

                   return;

               }


               var data = $.parseJSON(d);

               var blogMain = $('.blog-main');
               blogMain.empty();

               blogMain.append(data.content);
          });

       }