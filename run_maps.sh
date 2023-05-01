for file in '/data/Twitter dataset/'geoTwitter20-*.zip; do
	echo "running file"
	"$(./src/map.py --input_path="$file")"
	echo "finish running file"
done
