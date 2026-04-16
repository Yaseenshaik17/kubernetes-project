import urllib.request, json

# 1. Fetch current dashboard
req = urllib.request.Request("http://localhost:3000/api/dashboards/uid/ad9zxjk")
req.add_header("Authorization", "Basic YWRtaW46YWRtaW4=")
res = urllib.request.urlopen(req)
data = json.loads(res.read())
db = data["dashboard"]

# 2. Panels to delete
bad_titles = ["jvm misc", "jvm memory", "garbage collection", "classloading", "class loading", "buffer pools", "memory pools", "tomcat", "i/o overview", "log events", "file descriptors", "pause durations", "collections", "allocated/promoted"]

# Grafana can use rows or direct panels
new_panels = []
for p in db.get("panels", []):
    title = p.get("title", "").lower()
    
    # Check if panel title matches
    if any(bad in title for bad in bad_titles):
        continue
        
    # Check if type is row and its title matches
    if p.get("type") == "row" and any(bad in title for bad in bad_titles):
        continue
        
    # If the panel has nested panels (inside a row)
    if "panels" in p:
        p["panels"] = [sp for sp in p["panels"] if not any(bad in sp.get("title","").lower() for bad in bad_titles)]
        
    new_panels.append(p)

db["panels"] = new_panels

# 3. Post back
post_data = {"dashboard": db, "overwrite": True, "message": "Cleaned panels"}
req2 = urllib.request.Request("http://localhost:3000/api/dashboards/db", data=json.dumps(post_data).encode("utf-8"))
req2.add_header("Authorization", "Basic YWRtaW46YWRtaW4=")
req2.add_header("Content-Type", "application/json")
req2.add_header("Accept", "application/json")

rsp = urllib.request.urlopen(req2)
print("Dashboard updated:", rsp.read().decode())
