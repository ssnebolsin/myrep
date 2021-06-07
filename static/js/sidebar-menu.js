let bodyElement = null,
    customPointsMode = 'polygons';

const getCurrentDisplayMode = (element = null, defaultMode = 'block') => {
    if (element === null) {
        return null;
    } else {
        let currentDisplayMode = element.style.display;
        return (currentDisplayMode === '' || currentDisplayMode === null) ? defaultMode : currentDisplayMode;
    }
}

const showHideElement = (element = null,
                        displayMode = null,
                        defaultDisplayMode = null) => {
    if (element !== null) {
        if (displayMode === null) {
            switch(getCurrentDisplayMode(element, defaultDisplayMode)) {
                case 'none':
                    displayMode = defaultDisplayMode;
                    break;
                default:
                    displayMode = 'none';
                    break;
            }
        }
        element.style.display = displayMode;
    }
}

const hideByClassName = (className) => {
    Array.from(document.getElementsByClassName(className)).forEach((element) => {
        showHideElement(element.nextElementSibling, 'none', null);
    });
};

const openCLoseSubmenu = (element) => {
    element = element.nextElementSibling;
    let openClose = (getCurrentDisplayMode(element, null) === 'grid');
    hideByClassName('open-submenu');
    if (!openClose) {
        showHideElement(element, null, 'grid');
    }
};

const changeCustomPointsInputs = () => {
    let contentDiv = document.getElementById('custom-points-inputs'),
        customPointsDiv = document.getElementById('chosen-custom-points');
    if (customPointsMode === 'polygons') {
        customPointsMode = 'points';
        contentDiv.innerHTML = "<input id=\"point-long\" required type=\"number\" pattern=\"^[0-9]+[\\.]{1}[0-9]+$\" class=\"form-control\" placeholder=\"Довгота точки\" min=\"-180\" max=\"180\">" +
                            "<input id=\"point-lat\" required type=\"number\" pattern=\"^[0-9]+[\\.]{1}[0-9]+$\" class=\"form-control\" placeholder=\"Широта точки\" min=\"-90\" max=\"90\">";
    } else {
        customPointsMode = 'polygons';
        contentDiv.innerHTML = "<input id=\"polygon-id\" required type=\"number\" pattern=\"^[0-9]+$\" class=\"form-control\" placeholder=\"Номер полігона\" min=\"0\" max=\"10000000\">";
    }
    customPointsDiv.innerHTML = '';
};

const addCustomPoint = () => {
    let pointName = document.getElementById('point-name').value,
        pointContent = null;
    if (customPointsMode === 'polygons') {
        pointContent = "\"" + pointName + "\"<br>(" + document.getElementById('polygon-id').value + ")";
    } else {
        pointContent = "\"" + pointName + "\"<br>(" + document.getElementById('point-long').value + ',<br>' +
            document.getElementById('point-lat').value + ")";
    }
    let targetElement = document.getElementById('chosen-custom-points'),
        elementToAdd = document.createElement('div');
    elementToAdd.classList.add('point-visual');
    targetElement.appendChild(elementToAdd);
    elementToAdd.innerHTML = "<div>" + pointContent + "</div><div class=\"delete-point\" onclick=\"deleteCustomPoint(this)\">&Cross;</div>";
};

const deleteCustomPoint = (element) => {
    element.parentNode.remove();
};

window.onload = () => {
    bodyElement = document.getElementById('menu');
    showHideElement(bodyElement, 'none', null);
    document.getElementById('open-menu').addEventListener('click', () => {
        showHideElement(bodyElement, null, 'grid');
    });
    document.getElementById('reset-slicers-values').addEventListener('click', resetSlicers);
    document.getElementById('get-slicers-values').addEventListener('click', getSlicers);
    document.getElementById('set-slicers-values').addEventListener('click', setSlicers);
    hideByClassName('open-submenu');
    Array.from(document.getElementsByClassName('open-submenu')).forEach((element) => {
        element.addEventListener('click', () => {
            openCLoseSubmenu(element);
        });
    });
    document.getElementById('point-mode').addEventListener('change', changeCustomPointsInputs);
    document.getElementById('add-custom-point').addEventListener('click', addCustomPoint);
}