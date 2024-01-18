export default function getNeighborhoodsList() {
    this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

    this.addneighborhood = (newNeiighborhood) => {
        this.sanFranciscoNeighborhoods.push(newNeiighborhood);
        return this.sanFranciscoNeighborhoods;
    };
}