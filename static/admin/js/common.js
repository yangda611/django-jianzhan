  function JQ_post(id,url){
    var pattern = / \/|(pwd)|(\.html)|(\.com)|(script)|(select)|(from)|(print)|(\.js)|(http\:\/\/)|(https\:\/\/)|(www\.)|(\.\.\.)|(\/)|(\\)|(\$)/gim;
    var isMobile = /^(((1[3-9]{1}[0-9]{1}))+\d{8})$/;
    var isPhone = /^(?:(?:0\d{2,3})-)?(?:\d{7,8})(-(?:\d{3,}))?$/;
    var isEmail = /^(\w|\-)+@([a-zA-Z\d]+[-.])+([a-zA-Z0-9\u4E00-\u9FA5]+)$/;
    var flist = $("#"+id).serializeArray();
    var f = {};
    $.each(flist, function (i, field) {
        f[field.name] = field.value;
    });
    if($("#"+id+" input[name=guest]").length > 0 && (f.guest == '' || (/^[\u4E00-\u9FA5]{1,}$/).test(f.guest) == false || f.guest.toString().length > 4)){
        layer.msg('姓名必须为4个字以内的汉字');
        $('#'+id+' *[name=guest]').focus();
    }else if($("#"+id+" input[name=tel]").length > 0 && isPhone.test(f.tel) == false && isMobile.test(f.tel) == false){
        layer.msg('请输入正确的电话号码，如果是固话，区号和号码之间用 - 隔开');
        $('#'+id+' *[name=tel]').focus();
    }else if($("#"+id+" input[name=email]").length > 0 && f.email != '' && isEmail.test(f.email) == false){
        layer.msg('请输入您的正确邮箱');
        $('#'+id+' *[name=email]').focus();
    }else if($("#"+id+" *[name=content]").length > 0 && (f.content == '' || (/^[\dA-Za-z]+$/).test(f.content) || f.content.toString().length < 5 || f.content.toString().length > 200 || pattern.test(f.content))){
        layer.msg('留言内容不能含网址和非法字符、长度要在5-200个汉字之间');
        $('#'+id+' *[name=content]').focus();
    }else{
        var option = {
            url:url,
            type:'POST',
            dataType:'json',
            success : function(res) {
              if(res.status == 4){
                layer.open({
                    title:'提交成功',
                    content:res.msg,
                    scrollbar:false,
                    btnAlign:'c',
                    skin:'my_btn',
                    area:['340px','180px'],
                });
                $('#'+id)[0].reset();  // 提交成功重置
              } else {
                layer.msg(res.msg);
              }
            },
            fail:function (res){
                layer.msg(res.msg);
            }
        };
        $('#'+id).ajaxSubmit(option);
    }
}