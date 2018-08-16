import Axios from "axios";

const BASE_PATH = process.env.ACLU_API_BASE_URL;
export function getLayerData(){
	return Axios.get(href).then(response => {
		const features = response.data._items.map(item =>
			this.FeatureFactory.createFeature(item)
		);
};
