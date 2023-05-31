
# Specification of simple API to manage ETA (estimated time of arrival) of the ship to the destination point

It is crucial for a transportation company that its vessels arrive on time to the destination point. Timely arrival has a significant impact on the business performance and key metrics of the company. Using our __API__ you could ensures customer satisfaction and enhances the company's reputation, as clients rely on the prompt delivery of their goods. __Estimation of time of arrival__ allows you better planning and resource allocation, optimizing fleet utilization and minimizing idle time. Ultimately, the ability to consistently deliver cargo on time contributes to increased productivity, profitability, and a competitive edge in the transportation industry.

Our __API__ provides simple and effective approach for __estimation of time of arrival__. 

API specification consists of 4 requests using HTTP POST method:

1. Calculate theoretical __ETA__: 

`POST /calculate_eta`

2. Calculate real __ETA__: 

`POST /real_eta`

3. Ship speed calculation: 

`POST /speed`

4. Adjust the route: 

`POST /adjust_route`

## 1. Theoretical ETA using planned route specified by polyline and average speed

### Request

__POST__ `/calculate_eta`

#### Payload

- Content type: application/json

```json
{
	"route": [],
	"avgSpeed": "string"
}
```

 Item | Description 
 --- | --- 
 route | list of planned route points 
 avgSpeed | Average speed estimation 

### Response

- Content type: application/json

```json
{
	"eta": "string"
}

```
 Item | Description 
 --- | --- 
 eta | estimated time of arrival date and time 

### Request example (Python)

```python
import requests

data = {'route': [100, 200, 300],
        'avgSpeed': "20"
}
url = "http://<server>/calculate_eta"

r = requests.post(url, json=data)
```

### Request example (curl)

```bash
curl -X POST -H "Content-type: application/json" -d "{\"route\" : [100, 200, 300], \"avgSpeed\" : \"20\"}" "localhost:8080/calculate_eta"
```

## 2. Real ETA using real route specified by polyline in combination with remaining part of the planned route, time of departure and current time

### Request

__POST__ `/real_eta`

#### Payload

- Content type: application/json

```json
{
	"realRoute": [],
	"remainRoute": [],
	"departureTime": "2023-05-31T17:00:00",
	"currentTime": "2023-05-31T13:30:00"
}
```

### Response

- Content type: application/json

```json
{
	"realEta": "string"
}
```

## 3. Calculation of the speed of the ship, which is required to reach destination port till the specified ETA using the real and remaining part of the planned route

### Request

__POST__ `/speed`

#### Payload

- Content type: application/json

```json
{
	"realRoute": [],
	"remainRoute": [],
	"eta": "string"
}
```

### Response

- Content type: application/json

```json
{
	"speed": "string"
}
```

## 4. Adjust the route combining planned and real routes to minimize ETA and return the adjusted route as a polyline

### Request

__POST__ `/adjust_route`

#### Payload

- Content type: application/json

```json
{
	"realRoute": [],
	"plannedRoute": []
}
```

### Response

- Content type: application/json

```json
{
	"adjustedRoute": []
}
```

## Appendix

### Target audience:

- Software developers

### Strong and weak features of the API:

- Simple
- Stateless

### Possibilities to improve:

- Add more parameters

### Used SEO approach:

- keywords: API, ETA, estimated time of arrival
