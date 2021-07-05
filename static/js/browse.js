$(document).ready(function () {
    const filter_json_object = {}
    const current_url = window.location.href;
    const base_url = current_url.substr(0, current_url.lastIndexOf('/'));

    function createURLQueryToJson(url) {
        // given url to find all parameters and return json object.
        let _url = new URL(url);
        let _params = new URLSearchParams(_url.search);
        let json_data = Array.from(_params.keys()).reduce((sum, value) => {
            return Object.assign({
                [value]: _params.get(value).split(',')
            }, sum);
        }, {});
        return json_data;
    }

    function createJsonToURLQuery(o) {
        // given parameters json object and return encoded url.
        return Object.keys(o)
            .map(key => `${encodeURIComponent(key)}=` +
                o[key].map(v => encodeURIComponent(v)).join(','))
            .join('&')
    }

    $.each(createURLQueryToJson(current_url), function (key, val) {
        // on window load to get current url and checkbox checked if parameter in value give.
        var fecture_filter_html_block = $(".accordion-item." + key);
        if (product_length) {
            fecture_filter_html_block.find("button").removeClass('collapsed');
            fecture_filter_html_block.find("div.accordion-collapse.collapse").addClass('show');
        }
        $.each(val, function (index, fileter_val) {
            $(":checkbox[class='styled-checkbox'][name='" + key + "'][value='" +
                    fileter_val + "']")
                .attr("checked", true);
        });
    });

    $('.styled-checkbox').on('change', function () {
        // on filter any chcekbox checked or uncheck then genrate new url and window current location change to new url.
        $(".styled-checkbox:checked").each(function () {
            var filter_value = $(':checkbox[name=' + this.name + ']:checked').map(
                function () {
                    return this.value;
                }).get();
            filter_json_object[this.name] = filter_value;
        });
        window.location.href = base_url + '/?' + createJsonToURLQuery(filter_json_object);
    });

    $('.page-link-number').on('click', function () {
        // on filter by page number
        $(".styled-checkbox:checked").each(function () {
            var filter_value = $(':checkbox[name=' + this.name + ']:checked').map(
                function () {
                    return this.value;
                }).get();
            filter_json_object[this.name] = filter_value;
        });
        filter_json_object['page'] = [$(this).attr('value')];
        console.log(filter_json_object);
        window.location.href = base_url + '/?' + createJsonToURLQuery(filter_json_object);
    });
});