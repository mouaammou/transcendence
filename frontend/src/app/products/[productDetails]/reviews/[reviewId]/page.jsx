import { notFound } from "next/navigation";

const ReviewDetails = ({params}) => {
	if (params.reviewId > 1000) notFound();
	return <h1>
		reviews product {params.productDetails} with review number {params.reviewId}
	</h1>;
}
 
export default ReviewDetails;