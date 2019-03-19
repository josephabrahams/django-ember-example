import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    filterByCity(param) {
      // search
      if (param !== '') {
        return this.store.query('rental', {
          filter: {
            "city.icontains": param
          }
        }).then((filteredResults) => {
          return { query: param, results: filteredResults };
        });
      // default
      } else {
        return this.store.findAll('rental').then((results) => {
          return { query: param, results: results };
        });
      }
    }
  }
});
