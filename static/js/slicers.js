/* Тестова версія. Потрібно оптимізувати */
let currentSlicerState = null;

const getSlicers = () => {
    const embedContainer = $('#report-container')[0];
    report = powerbi.get(embedContainer);
    try {
        report.getPages().then((pagesList) => {
            const activePage = pagesList.filter((page) => {
                return page.isActive;
            })[0];
            activePage.getVisuals().then((visualsList) => {
                Array.from(visualsList).forEach((visual) => {
                    if (visual.type === 'slicer') {
                        visual.getSlicerState().then((slicerState) => {
                            if (slicerState['filters'][0] != undefined && visual.name === '9a917e3a4719f5c3103a') {
                                currentSlicerState = slicerState['filters'][0];
                                let conditions = slicerState['filters'][0];
                                let upperBound = 'Operator - ' + conditions['operator'] + ', value - ' +
                                                conditions['values'][0];
                                window.alert(upperBound);
                            }
                        }, (slicerError) => {
                            console.log('Something went wrong: ', slicerError);
                        });
                    }
                });
            }, (visualsError) => {
                console.log('Something went wrong: ', visualsError);
            });
        }, (pagesError) => {
            console.log('Something went wrong: ', pagesError);
        });
    }
    catch(errors) {
        console.log(errors);
    }
}

const setSlicers = () => {
    const regexp = /^[А-Яа-яії]+$/
    const lowerBound = window.prompt('Введіть назву області');
    (regexp.test(lowerBound) || currentSlicerState !== null) ? '' : window.alert('Invalid value! Attribute value will be set to Київська');
    const filter = currentSlicerState === null ? {
      $schema: "http://powerbi.com/product/schema#basic",
      target: {
        table: "Dataset",
        column: "region_name_ua"
      },
      operator: "In",
      values: [regexp.test(lowerBound) ? lowerBound : "Київська"],
    } : currentSlicerState;
    let embedContainer = $('#report-container')[0];
    report = powerbi.get(embedContainer);
    try {
        const pages = report.getPages();
        pages.then((pagesList) => {
            const activePage = pagesList.filter((page) => {
                return page.isActive;
            })[0];
            activePage.getVisuals().then((visualsList) => {
                let visual = visualsList.filter((visual) => {
                    return visual.type === 'slicer' && visual.name === '9a917e3a4719f5c3103a';
                })[0];
                visual.setSlicerState({filters: [filter]});
                window.alert('Slicer was updated successfully');
            }, (visualsError) => {
                console.log('Something went wrong :', visualsError);
            });
        }, (pagesError) => {
            console.log('Something went wrong :', pagesError);
        });
    }
    catch (errors) {
        console.log(errors);
    }
}

const resetSlicers = () => {
    currentSlicerState = null;
    let embedContainer = $('#report-container')[0];
    report = powerbi.get(embedContainer);
    try {
        const pages = report.getPages();
        pages.then((pagesList) => {
            const activePage = pagesList.filter((page) => {
                return page.isActive;
            })[0];
            activePage.getVisuals().then((visualsList) => {
                let visual = visualsList.filter((visual) => {
                    if (visual.type === 'slicer') {
                        try {
                            visual.setSlicerState({filters: []});
                        } catch (resetError) {
                            console.log('Something went wrong :', resetError);
                        }
                    }
                })[0];
                window.alert('Slicers were updated successfully');
            }, (visualsError) => {
                console.log('Something went wrong :', visualsError);
            });
        }, (pagesError) => {
            console.log('Something went wrong :', pagesError);
        });
    }
    catch (errors) {
        console.log(errors);
    }
}