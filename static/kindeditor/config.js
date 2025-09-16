
KindEditor.ready(function(K) {
        // K.create('textarea[name=content]', {
        K.create('#id_content', {
            width: 'calc(100% - 180px)',
            displau:'inline-block',
            height: '400px',
            uploadJson: '/admin/upload/kindeditor',
        });
});